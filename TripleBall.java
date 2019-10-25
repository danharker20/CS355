import java.awt.Color;

public class TripleBall extends BasicBall
{
	int numHits;
	
	public TripleBall(double r, Color c)
	{
		super(r, c);
		
		numHits = 0;
	}
	
	@Override
	public int reset()
	{
		numHits++;
		
		// IF HIT 3 TIMES, RESET
		if (numHits >= 3)
		{
			rx = 0.0;
	        ry = 0.0;
	        vx = StdRandom.uniform(-0.01, 0.01);
	        vy = StdRandom.uniform(-0.01, 0.01);
	        
	        numHits = 0;
		}
		
        
        return 1;
	}	
	
	@Override
	public int getScore()
	{
		return 100;
	}
}
