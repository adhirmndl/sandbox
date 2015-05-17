package patterns;

import ducks.MallardDuck;
import ducks.RedheadDuck;
import ducks.DuckCall;
import ducks.RubberDuck;

public class CountingDuckFactory extends AbstractDuckFactory {
	public Quackable createMallardDuck(){
		return new QuackCounter(new MallardDuck());
	}
	public Quackable createRedheadDuck(){
		return new QuackCounter(new RedheadDuck());
	}
	public Quackable createDuckCall(){
		return new QuackCounter(new DuckCall());
	}
	public Quackable createRubberDuck(){
		return new QuackCounter(new RubberDuck());
	}
}