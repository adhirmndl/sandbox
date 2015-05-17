package test;

import patterns.Quackable;
import patterns.GooseAdapter;
import patterns.QuackCounter;
import patterns.CountingDuckFactory;
import patterns.AbstractDuckFactory;
import patterns.Flock;

import other.Goose;

public class DuckSimulator {
	public static void main (String[] args){
		DuckSimulator dsim = new DuckSimulator();
		AbstractDuckFactory duckFactory = new CountingDuckFactory();
		dsim.simulate(duckFactory);
	}

	void simulate(AbstractDuckFactory duckFactory){

		Quackable redheadDuck = duckFactory.createRedheadDuck();
		Quackable duckCall    = duckFactory.createDuckCall();
		Quackable rubberDuck  = duckFactory.createRubberDuck();
		Quackable gooseDuck   = new GooseAdapter(new Goose());

		System.out.println("\nDuck Simulator");

		Flock flockOfDucks    = new Flock();

		flockOfDucks.add(redheadDuck);
		flockOfDucks.add(duckCall);
		flockOfDucks.add(rubberDuck);
		flockOfDucks.add(gooseDuck);

		Flock flockOfMallards = new Flock();

		Quackable mallardOne   = duckFactory.createMallardDuck();
		Quackable mallardTwo   = duckFactory.createMallardDuck();
		Quackable mallardThree = duckFactory.createMallardDuck();
		Quackable mallardFour  = duckFactory.createMallardDuck();

		flockOfMallards.add(mallardOne);
		flockOfMallards.add(mallardTwo);
		flockOfMallards.add(mallardThree);
		flockOfMallards.add(mallardFour);

		flockOfDucks.add(flockOfMallards);

		System.out.println("\nDuck Simulator : Whole Flock");
		simulate(flockOfDucks);

		System.out.println("\nDuck Simulator : Mallard Flock");
		simulate(flockOfMallards);

		System.out.println("Number of Quacks : " + QuackCounter.getQuacks());
	}

	void simulate(Quackable duck){
		duck.quack();
	}
}