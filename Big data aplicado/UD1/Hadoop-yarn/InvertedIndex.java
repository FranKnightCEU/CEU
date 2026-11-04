import java.io.IOException;
import java.util.HashSet;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.FileSplit;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class InvertedIndex {

    // 1. MAPPER: Extrae el nombre del archivo origen y emite (palabra, nombre_archivo)
    public static class IndexMapper extends Mapper<LongWritable, Text, Text, Text> {
        private Text wordKey = new Text();
        private Text docValue = new Text();

        @Override
        public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
            // Obtener el nombre del archivo actual en HDFS usando FileSplit
            FileSplit fileSplit = (FileSplit) context.getInputSplit();
            String fileName = fileSplit.getPath().getName();
            docValue.set(fileName);

            // Limpieza del texto y division en palabras
            String line = value.toString().replaceAll("[^a-zA-Z0-9\\s]", "").toLowerCase();
            String[] words = line.split("\\s+");

            for (String w : words) {
                if (!w.trim().isEmpty()) {
                    wordKey.set(w);
                    context.write(wordKey, docValue);
                }
            }
        }
    }

    // 2. REDUCER: Desduplica los nombres de archivo y emite (palabra, "doc1.txt, doc2.txt")
    public static class IndexReducer extends Reducer<Text, Text, Text, Text> {
        private Text result = new Text();

        @Override
        public void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
            HashSet<String> uniqueDocs = new HashSet<>();

            // Agrupar y desduplicar archivos para la palabra clave
            for (Text val : values) {
                uniqueDocs.add(val.toString());
            }

            // Construir la cadena delimitada por comas
            StringBuilder docList = new StringBuilder();
            for (String doc : uniqueDocs) {
                if (docList.length() > 0) {
                    docList.append(", ");
                }
                docList.append(doc);
            }

            result.set(docList.toString());
            context.write(key, result);
        }
    }

    // 3. DRIVER: Configuracion del trabajo en YARN
    public static void main(String[] args) throws Exception {
        if (args.length != 2) {
            System.err.println("Uso: InvertedIndex <directorio_entrada_hdfs> <salida_hdfs>");
            System.exit(-1);
        }

        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "Indice Invertido");

        job.setJarByClass(InvertedIndex.class);
        job.setMapperClass(IndexMapper.class);
        job.setReducerClass(IndexReducer.class);

        // Tipos de salida del Mapper y Reducer (Text, Text)
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);

        // Asignacion de rutas HDFS con los indices de args
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}