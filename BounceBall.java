import java.awt.Color;

public class BounceBall extends BasicBall 
{
	private int numBounces;
	public boolean isOut;
	
	//Constructor
	public BounceBall(double r, Color c)
	{
		super(r, c);
		
		numBounces = 0;
		isOut = false;
	}
	
	@Override
	public void move() 
    {
        rx = rx + vx;
        ry = ry + vy;
        
        //System.out.print(Math.abs(rx) + " " + Math.abs(ry) + "\n"); //just a check 
        
        //change vx
        if ((Math.abs(rx) >= (1.0 - radius)))
        {
        	if (numBounces < 3)
        	{  		
        		vx *= -1;        		
        		numBounces++;
        	}
        }
        
        //change vy
        else if ((Math.abs(ry) >= (1.0 - radius)))
        {
        	if (numBounces < 3)
        	{
        		vy *= -1;
        		numBounces++;
        	}
        }
        
    	else
    	{
    		isOut = true;
    	}      	
    }

	@Override
	public int getScore() 
    {
    	return 15;
    }
}
