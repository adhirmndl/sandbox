package ducks;

import patterns.Quackable;
import patterns.Observer;
import patterns.Observable;

public class RedheadDuck implements Quackable {

	Observable observable;

	public RedheadDuck(){
		this.observable = new Observable(this);
	}
	public void quack(){
		System.out.println("Quack");
		notifyObservers();

	}

	public void registerObserver(Observer obs){
		this.observable.registerObserver(obs);
	}

	public void notifyObservers(){
		this.observable.notifyObservers();
	}
}