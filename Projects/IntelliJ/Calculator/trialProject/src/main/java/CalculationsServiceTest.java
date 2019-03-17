import org.junit.Assert;
import org.junit.Test;

public class CalculationsServiceTest {
    @Test
    public void addTest(){
        int num1 = 9;
        int num2 = 4;
        int numExpected = 13;
        int numActual = CalculationsService.add(num1, num2);
        Assert.assertEquals(numExpected, numActual);
    }
}
