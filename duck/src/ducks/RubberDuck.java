package ducks;

import patterns.Quackable;
import patterns.Observer;
import patterns.Observable;

public class RubberDuck implements Quackable {
	Observable observable;

	public RubberDuck(){
		this.observable = new Observable(this);
	}
	public void quack(){
		System.out.println("Squeak");
		notifyObservers();
	}

	public void registerObserver(Observer obs){
		this.observable.registerObserver(obs);
	}

	public void notifyObservers(){
		this.observable.notifyObservers();
	}
}