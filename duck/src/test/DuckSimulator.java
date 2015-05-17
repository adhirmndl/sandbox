package test;

import ducks.Quackable;
import ducks.MallardDuck;
import ducks.RedheadDuck;
import ducks.DuckCall;
import ducks.RubberDuck;

public class DuckSimulator {
	public static void main (String[] args){
		DuckSimulator dsim = new DuckSimulator();
		dsim.simulate();
	}

	void simulate(){
		Quackable mallardDuck = new MallardDuck();
		Quackable redheadDuck = new RedheadDuck();
		Quackable duckCall    = new DuckCall();
		Quackable rubberDuck  = new RubberDuck();

		System.out.println("\nDuck Simulator");

		simulate(mallardDuck);
		simulate(redheadDuck);
		simulate(duckCall);
		simulate(rubberDuck);
	}

	void simulate(Quackable duck){
		duck.quack();
	}
}