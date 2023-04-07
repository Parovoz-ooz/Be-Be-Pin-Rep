public class Main {


    private final double BIAS = -1.3;
    private final double WEIGHTS = 2.3;
    private int numLayers;
    private int[] sizes;


    public Main(int... sizes)
    {
        this.sizes = sizes;
        this.numLayers = sizes.length;
    }


    public static void main(String[] args)
    {
        Main net = new Main(2, 3, 2);
        double[] inputs = { 1, 1 };
        double[] outputs = net.feedForward(inputs);


        for (int i = 0; i < outputs.length; i++)
        { // выводит выходной массив, состоящий из чисел с плавающей точкой от 0 до 1
            System.out.println(outputs[i]);
        }
    }


    private double[] feedForward(double[] inputs)
    {
        double[] outputs = null;
        for (int i = 1; i < numLayers; i++)
        { // выполняется итерация по всем слоям (кроме первого, поскольку это входной слой)
            int size = sizes[i];
            double[] z = new double[size];
            outputs = new double[size];
            for (int j = 0; j < size; j++)
            { // выполняет итерацию по всем нейронам слоя i
                for (int k = 0; k < inputs.length; k++)
                { // выполняет итерацию по всем входным данным для уровня i
                    z[j] += WEIGHTS * inputs[k];
                }
                z[j] += BIAS;
                outputs[j] = 1 / (1 + Math.exp(-z[j]));
            }
            inputs = outputs;
        }
        return outputs;
    }
}
