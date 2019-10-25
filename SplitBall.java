import java.awt.Color;

public class SplitBall extends BasicBall
{
	//Constructor
	public SplitBall(double r, Color c)
	{
		super(r, c);
	}
	
	@Override
	public int getScore() 
    {
    	return 10;
    }
}
