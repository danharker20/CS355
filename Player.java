import java.util.Arrays;

public class Player 
{
	private int score;
	private int totalHits;
	private int numHitsBasicBall;
	private int numHitsBounceBall;
	private int numHitsShrinkBall;
	private int numHitsSplitBall;
	private int numHitsTripleBall;
	
	// Constructor
	public Player()
	{
		score = 0;
		totalHits = 0;
		numHitsBasicBall = 0;
		numHitsBounceBall = 0;
		numHitsShrinkBall = 0;
		numHitsSplitBall = 0;
		numHitsTripleBall = 0;
	}
	
	// SETS	
	public void setScore(int value)//called whenever a ball's position is reset to (0,0)
	{
		score += value;
	}
	public void setNumHitsBasicBall()
	{
		numHitsBasicBall++;
	}	
	public void setNumHitsBounceBall()
	{
		numHitsBounceBall++;
	}
	public void setNumHitsShrinkBall()
	{
		numHitsShrinkBall++;
	}
	public void setNumHitsSplitBall()
	{
		numHitsSplitBall++;
	}
	public void setNumHitsTripleBall()
	{
		numHitsTripleBall++;
	}
	public void setTotalHits()
	{
		totalHits++;
	}

	// GETS
	public int getScore()
	{
		return score;
	}
	public int getTotalHits()
	{
		return totalHits;
	}
	public int getNumHitsBasicBall()
	{
		return numHitsBasicBall;
	}
	public int getNumHitsBounceBall()
	{
		return numHitsBounceBall;
	}
	public int getNumHitsShrinkBall()
	{
		return numHitsShrinkBall;
	}
	public int getNumHitsSplitBall()
	{
		return numHitsSplitBall;
	}
	public int getNumHitsTripleBall()
	{
		return numHitsTripleBall;
	}
	public String getMostHitBall()
	{
		int allHits[] = new int[5];
		
		allHits[0] = numHitsBasicBall;
		allHits[1] = numHitsBounceBall;
		allHits[2] = numHitsShrinkBall;
		allHits[3] = numHitsSplitBall;
		allHits[4] = numHitsTripleBall;
		
		Arrays.sort(allHits);
		
		int mostHitBall = allHits[4]; //gets last num because it's the biggest
		
		
		if (mostHitBall == numHitsBasicBall)
		{
			return "Basic Ball";
		}
			
		else if (mostHitBall == numHitsBounceBall)
		{
			return "Bounce Ball";
		}
		
		else if (mostHitBall == numHitsShrinkBall)
		{
			return "Shrink Ball";
		}
				
		else if (mostHitBall == numHitsSplitBall)
		{
			return "Split Ball";
		}
		
		else
		{
			return "Triple Ball";
		}
				
	}
	
}
