import requests
import math
import urllib.parse

# 🌐 URL COMPLETA OFICIAL (Con la ruta de la API v2 incluida)
BASE_URL = "https://pokeapi.co/api/v2"

# --- FUNCIONES DE CONEXIÓN A LA API ---

def get_pokemon_complete_data(name):
    """Extrae tipos y estadísticas base directamente desde los servidores de la PokéAPI."""
    nombre_limpio = str(name).lower().strip()
    nombre_seguro = urllib.parse.quote(nombre_limpio)

    try:
        # Se genera la ruta exacta limpia: https://pokeapi.co/api/v2/pokemon/tyranitar
        url_final = f"{BASE_URL}/pokemon/{nombre_seguro}"
        r = requests.get(url_final, timeout=5)
        
        if r.status_code != 200:
            raise ValueError(
                f"❌ Error 404: El servidor no reconoció el nombre.\n"
                f"URL exacta intentada: {r.url}\n"
                f"Asegúrate de que BASE_URL incluya /api/v2"
            )
            
        data = r.json()
        return {
            "name": data["name"],
            "types": [t["type"]["name"] for t in data["types"]],
            "stats": {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}
        }
    except requests.exceptions.ConnectionError:
        raise RuntimeError("❌ Error de conexión: No se pudo conectar a la PokéAPI. Revisa tu acceso a internet.")
    except requests.exceptions.Timeout:
        raise RuntimeError("⏳ La PokéAPI tardó demasiado en responder.")

def get_move_complete_data(name):
    """Extrae los detalles técnicos del movimiento desde la API de forma segura."""
    mov_limpio = str(name).lower().replace(' ', '-').strip()
    mov_seguro = urllib.parse.quote(mov_limpio)
    try:
        url_final = f"{BASE_URL}/move/{mov_seguro}"
        r = requests.get(url_final, timeout=5)
        if r.status_code != 200:
            raise ValueError(f"Movimiento '{name}' no encontrado en la API (Error {r.status_code}). URL: {r.url}")
        data = r.json()
        return {
            "name": data["name"],
            "power": data.get("power"),
            "type": data["type"]["name"],
            "damage_class": data["damage_class"]["name"]
        }
    except requests.exceptions.Timeout:
        raise RuntimeError("⏳ La PokéAPI no respondió a tiempo para el movimiento.")

def get_type_effectiveness(move_type, target_types):
    """Calcula el multiplicador analizando dinámicamente las debilidades en la API."""
    try:
        url_final = f"{BASE_URL}/type/{move_type}"
        r = requests.get(url_final, timeout=5)
        if r.status_code != 200:
            return 1.0
        damage_relations = r.json()["damage_relations"]
        
        double_damage = [t["name"] for t in damage_relations["double_damage_to"]]
        half_damage = [t["name"] for t in damage_relations["half_damage_to"]]
        no_damage = [t["name"] for t in damage_relations["no_damage_to"]]
        
        mult = 1.0
        for t in target_types:
            if t in double_damage: mult *= 2.0
            elif t in half_damage: mult *= 0.5
            elif t in no_damage: mult *= 0.0
        return mult
    except requests.exceptions.Timeout:
        return 1.0

# --- FUNCIONES MATEMÁTICAS ---

def apply_modifier(stat, stage):
    """Aplica los modificadores de nivel en combate (-6 a +6)."""
    if stage >= 0:
        return math.floor(stat * ((2 + stage) / 2))
    else:
        return math.floor(stat * (2 / (2 - stage)))

def poke_round(value):
    """Aplica el truncamiento reglamentario hacia abajo de las consolas de Nintendo."""
    return math.floor(value)

# --- NÚCLEO DEL CÁLCULO DE DAÑO COMPETITIVO ---

def calcular_danio_profesional(
    p_atacante, p_defensor, m_nombre, 
    lvl_atk=50, lvl_def=50,
    evs_atk=252, ivs_atk=31, naturaleza_atk=1.0, stage_atk=0,
    evs_def=252, ivs_def=31, naturaleza_def=1.0, stage_def=0,
    critico=False, quemado=False,
    clima="none", terreno="none",
    objeto_atk="none", habilidad_atk="none", habilidad_def="none"
):
    # 1. Peticiones de datos reales
    atk_data = get_pokemon_complete_data(p_atacante)
    def_data = get_pokemon_complete_data(p_defensor)
    move = get_move_complete_data(m_nombre)
    
    if move["power"] is None:
        print(f"⚠️ El movimiento '{move['name']}' es de estado. No calcula daño directo.")
        return None

    # 2. Stats en combate calculados desde los valores base de la API
    is_physical = move["damage_class"] == "physical"
    stat_atk_base = atk_data["stats"]["attack"] if is_physical else atk_data["stats"]["special-attack"]
    stat_def_base = def_data["stats"]["defense"] if is_physical else def_data["stats"]["special-defense"]
    
    atk_final = math.floor((math.floor((2 * stat_atk_base + ivs_atk + math.floor(evs_atk / 4)) * lvl_atk / 100) + 5) * naturaleza_atk)
    def_final = math.floor((math.floor((2 * stat_def_base + ivs_def + math.floor(evs_def / 4)) * lvl_def / 100) + 5) * naturaleza_def)
    
    if critico:
        real_stage_atk = max(0, stage_atk)
        real_stage_def = min(0, stage_def)
    else:
        real_stage_atk = stage_atk
        real_stage_def = stage_def
        
    atk_final = apply_modifier(atk_final, real_stage_atk)
    def_final = apply_modifier(def_final, real_stage_def)

    # 3. Potencia Base (BP)
    bp = move["power"]
    
    if terreno == "electric" and move["type"] == "electric": bp = poke_round(bp * 1.3)
    elif terreno == "grassy" and move["type"] == "grass": bp = poke_round(bp * 1.3)
    elif terreno == "psychic" and move["type"] == "psychic": bp = poke_round(bp * 1.3)
    elif terreno == "misty" and move["type"] == "dragon": bp = poke_round(bp * 0.5)

    if objeto_atk == "choice_band" and is_physical: atk_final = poke_round(atk_final * 1.5)
    if objeto_atk == "choice_specs" and not is_physical: atk_final = poke_round(atk_final * 1.5)

    if habilidad_atk == "guts" and quemado and is_physical: atk_final = poke_round(atk_final * 1.5)
    if habilidad_def == "fluffy" and is_physical: def_final = poke_round(def_final * 2.0)

    # 4. Fórmula Base
    base_damage = poke_round(poke_round(poke_round(2 * lvl_atk / 5 + 2) * bp * atk_final / def_final) / 50) + 2

    # 5. Modificadores de entorno
    if quemado and is_physical and habilidad_atk != "guts":
        base_damage = poke_round(base_damage * 0.5)
        
    if clima == "sun" and move["type"] == "fire": base_damage = poke_round(base_damage * 1.5)
    elif clima == "sun" and move["type"] == "water": base_damage = poke_round(base_damage * 0.5)
    elif clima == "rain" and move["type"] == "water": base_damage = poke_round(base_damage * 1.5)
    elif clima == "rain" and move["type"] == "fire": base_damage = poke_round(base_damage * 0.5)

    if critico:
        base_damage = poke_round(base_damage * 1.5)

    if objeto_atk == "life_orb":
        base_damage = poke_round(base_damage * 1.3)

    # 6. Multiplicadores Finales (STAB y Tabla de tipos)
    stab_mult = 1.0
    if move["type"] in atk_data["types"]:
        stab_mult = 2.0 if habilidad_atk == "adaptability" else 1.5

    type_mult = get_type_effectiveness(move["type"], def_data["types"])

    # 7. Los 16 Rolls oficiales (85% al 100%)
    rango_danio = []
    for r in range(85, 101):
        d_final = poke_round(poke_round(base_damage * r / 100) * stab_mult * type_mult)
        rango_danio.append(d_final)
        
    # Impresión en terminal
    print(f"\n ⚔️  {atk_data['name'].upper()} vs 🛡️  {def_data['name'].upper()} usando {move['name'].upper()}")
    print(f"Tipos Atacante: {atk_data['types']} | Tipos Defensor: {def_data['types']}")
    print(f"Efectividad: x{type_mult} | STAB: x{stab_mult} | Crítico: {critico}")
    print(f"Clima: {clima} | Terreno: {terreno} | Objeto Atk: {objeto_atk}")
    print("-" * 65)
    print(f"📉 Mínimo Daño Posible: {rango_danio[0]} PS")
    print(f"📈 Máximo Daño Posible: {rango_danio[-1]} PS")
    print(f"📋 Rango completo de los 16 rodajes (Rolls): {rango_danio}\n")
    
    return rango_danio

# --- EJECUCIÓN DEL COMBATE ---
# Escenario: Tyranitar usando Terremoto (Earthquake) contra Aggron
resultados = calcular_danio_profesional(
    p_atacante="tyranitar", 
    p_defensor="aggron", 
    m_nombre="earthquake",    
    lvl_atk=50, evs_atk=252, naturaleza_atk=1.1, stage_atk=0,  
    lvl_def=50, evs_def=252, naturaleza_def=1.0, stage_def=0,  
    critico=False, 
    clima="none",               
    terreno="none", 
    objeto_atk="none"   
)
