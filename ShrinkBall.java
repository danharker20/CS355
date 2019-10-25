import java.awt.Color;

public class ShrinkBall extends BasicBall
{
	double shrinkSize;
	double originalRadius;
	
	// Constructor
	public ShrinkBall(double r, Color c)
	{
		super(r, c);
		
		shrinkSize = 0.67;
		originalRadius = r;
	}
	
	@Override
	public int reset()
	{
		rx = 0.0;
        ry = 0.0;
        vx = StdRandom.uniform(-0.01, 0.01);
        vy = StdRandom.uniform(-0.01, 0.01);
        
        //change radius
        if ((radius * shrinkSize) < (originalRadius * 0.25))
        	radius = originalRadius;
        else
        	radius *= shrinkSize;
        
        return 1;
	}
	
	@Override
	public int getScore() 
    {
    	return 20;
    }
}
