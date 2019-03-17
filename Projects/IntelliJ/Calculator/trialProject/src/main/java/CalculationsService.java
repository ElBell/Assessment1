public class CalculationsService {
    public CalculationsService(int given) {
        storedMethod = given;
    }
    public int getStoredMethod() {
        return storedMethod;
    }

    public void setStoredMethod(int storedMethod) {
        this.storedMethod = storedMethod;
    }
    public static int add(int n1, int n2) {return n1+n2;}

    private int storedMethod = 0;

}
