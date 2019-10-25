/******************************************************************************
 *  Compilation:  javac BallGame.java
 *  Execution:    java BallGame n
 *  Dependencies: BasicBall.java StdDraw.java
 *
 *  Creates a BasicBall and animates it
 *
 *  Part of the animation code is adapted from Computer Science:   An Interdisciplinary Approach Book
 *  
 *  Run the skeleton code with arguments : 1  basic  0.08
 *******************************************************************************/
import java.awt.Color;
import java.awt.Font;

import java.util.ArrayList;

public class BallGame
{	
    public static void main(String[] args) 
    {     	
    	ArrayList<String> ballsInfo = new ArrayList <String> (); //could probably an Array but I don't wanna redo it
    	
    	// PUT EVERYTHING FROM THE RUN CONFIGURATION LINE INTO "ballInfo"
    	for (int i=0; i < args.length; i ++)
    	{    		
    		ballsInfo.add(args[i]);
    	}
    	
    	// GET "totalBalls" AMOUNT
    	int totalBalls = Integer.parseInt(ballsInfo.remove(0));
    	    	
    	// ADD ALL BALLTYPES TO "ballTypes[]"
    	// ADD ALL BALLSIZES to "ballSizes[]"
    	String ballTypes[] = new String[totalBalls];
    	double ballSizes[] = new double[totalBalls];    	
    	int j = 0;
    	int k = 0;
    	
    	for (int i = 0; i < ballsInfo.size(); i++)
    	{    		
    		if (i%2 == 0)
    		{
    			ballTypes[j] = ballsInfo.get(i);
    			j++;
    		}
    		
    		else
    		{
    			ballSizes[k] = Double.parseDouble(ballsInfo.get(i));
    			k++;
    		}
    	}
    	   	
    	//CREATE NEW BALLS, PUT THEM IN "gameBalls"	
    	ArrayList<BasicBall> gameBalls = new ArrayList <BasicBall> ();
    	
    	for (int i=0; i < totalBalls; i++)
    	{
    		if ((ballTypes[i].toString()).equals("basic"))
    		{
    			BasicBall newBasicBall = new BasicBall(ballSizes[i], Color.RED);
    			gameBalls.add(newBasicBall);
    		}
    		
    		else if ((ballTypes[i].toString()).equals("shrink"))
    		{
    			ShrinkBall newShrinkBall = new ShrinkBall(ballSizes[i], Color.GREEN);
    			gameBalls.add(newShrinkBall);
    		}
    		
    		else if ((ballTypes[i].toString()).equals("split"))
    		{
    			SplitBall newSplitBall = new SplitBall(ballSizes[i], Color.YELLOW);
    			gameBalls.add(newSplitBall);
    		}
    			
    		else if ((ballTypes[i].toString()).equals("bounce"))
    		{
    			BounceBall newBounceBall = new BounceBall(ballSizes[i], Color.BLUE);
    			gameBalls.add(newBounceBall);
    		}
    		
    		else if ((ballTypes[i].toString()).equals("triple"))
    		{
    			TripleBall newTripleBall = new TripleBall(ballSizes[i], Color.WHITE);
    			gameBalls.add(newTripleBall);
    		}
    	}
    	
    	// CREATE PLAYER OBJECT FOR STATS
    	Player player = new Player();
    	    	
    	// NUMBER OF ACTIVE BALLS
    	int numBallsinGame = totalBalls;
        StdDraw.enableDoubleBuffering();
        
        // MAKE THE GAME WINDOW
        StdDraw.setCanvasSize(800, 800);
        // set boundary to box with coordinates between -1 and +1
        StdDraw.setXscale(-1.0, +1.0);
        StdDraw.setYscale(-1.0, +1.0);
   		
        // DO ANIMATION LOOP
        StdDraw.enableDoubleBuffering();
        while (numBallsinGame > 0) 
        {
        	// MOVE ALL BALLS
        	for (int i=0; i < gameBalls.size(); i++)
        	{       
        		
        		gameBalls.get(i).move();
        	}

            // CHECK IF MOUSE IS CLICKED
            if (StdDraw.isMousePressed()) 
            {
                double x = StdDraw.mouseX();
                double y = StdDraw.mouseY();
                
                // FOR EACH BALL, CHECK IF HIT
                for (int i=0; i < gameBalls.size(); i++)
                {
	                if (gameBalls.get(i).isHit(x,y))
	                {	 
	                	// RESET THE BALL
	                	gameBalls.get(i).reset();
	                	
	                	// DO BALL SPECIFIC STUFF
	                	if (gameBalls.get(i).getClass().getTypeName() == "BasicBall")
	                	{	                		
	                		player.setNumHitsBasicBall();
	                	}
	                	
	                	else if (gameBalls.get(i).getClass().getTypeName() == "BounceBall")
	                	{
	                		player.setNumHitsBounceBall();
	                	}
	                	
	                	else if (gameBalls.get(i).getClass().getTypeName() == "ShrinkBall")
	                	{
	                		player.setNumHitsShrinkBall();
	                	}
	                	
	                	else if (gameBalls.get(i).getClass().getTypeName() == "SplitBall")
	                	{
	                		player.setNumHitsSplitBall();
	                		
	                		//ADD NEW SPLITBALL TO THE GAME
	                		SplitBall newSplitBall = new SplitBall(gameBalls.get(i).getRadius(), Color.YELLOW);
	                		gameBalls.add(newSplitBall);
	                		totalBalls++;
	                	}
	                	
	                	else if (gameBalls.get(i).getClass().getTypeName() == "TripleBall")
	                	{
	                		//TODO: player.setNumHitsSplitBall();
	                	}
	                	
                    	// UPDATE PLAYER STATISTICS
                    	player.setTotalHits(); //add to total hits
                    	player.setScore(gameBalls.get(i).getScore()); //update score with corresponding ball points                  	
	                }
                }
            }
                
            numBallsinGame = 0;
            
            // DRAW THE N BALLS
            StdDraw.clear(StdDraw.GRAY);
            StdDraw.setPenColor(StdDraw.BLACK);
            
            // CHECK IF EACH BALL IF VISIBLE. IF VISIBLE, KEEP DRAWING
            // "numBallsinGame" HOLDS NUMBER OF VISIBLE BALLS IN GAME
            for (int i=0; i < gameBalls.size(); i++)
            {            	
	            if (gameBalls.get(i).isOut == false)
	            {
	            	gameBalls.get(i).draw();
	                numBallsinGame++;
	            }
            }
            
            // GAME PROGRESS and STATS
            StdDraw.setPenColor(StdDraw.YELLOW);
            Font font = new Font("Arial", Font.BOLD, 20);
            StdDraw.setFont(font);
            StdDraw.text(-0.65, 0.90, "Number of balls in game: "+ String.valueOf(numBallsinGame));
            
            // DISPLAY PLAYER STATS
            StdDraw.text(-0.65, 0.84, "Number of hits: " + String.valueOf(player.getTotalHits())); //this should be right???
            StdDraw.text(-0.65, 0.78, "Score: " + String.valueOf(player.getScore())); //this should be right????

            StdDraw.show();
            StdDraw.pause(20);
        }
        
        // GAME OVER
        while (true) 
        {
        	// CLEAR SCREEN
        	StdDraw.clear(StdDraw.GRAY);
        	
        	// PRINT "GAME OVER"
            StdDraw.setPenColor(StdDraw.BLUE);
            Font font = new Font("Arial", Font.BOLD, 60);
            StdDraw.setFont(font);
            StdDraw.text(0, 0, "GAME OVER");
            
            // PRINT PLAYER STATS
            font = new Font("Arial", Font.BOLD, 30);
            StdDraw.setFont(font);
            StdDraw.text(0, -0.11, "Total Hits: " + String.valueOf(player.getTotalHits()));
            StdDraw.text(0, -0.22, "Score: " + String.valueOf(player.getScore()));  
            StdDraw.text(0, -0.33, "Most hit ball: " + String.valueOf(player.getMostHitBall()));
            
            StdDraw.show();
            StdDraw.pause(10);           
        } 
    }
    

}
