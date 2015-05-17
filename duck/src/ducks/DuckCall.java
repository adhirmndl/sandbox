package ducks;

import patterns.Quackable;
import patterns.Observer;
import patterns.Observable;

public class DuckCall implements Quackable {
	Observable observable;

	public DuckCall(){
		this.observable = new Observable(this);
	}
	public void quack(){
		System.out.println("Kwak");
		notifyObservers();
	}

	public void registerObserver(Observer obs){
		this.observable.registerObserver(obs);
	}

	public void notifyObservers(){
		this.observable.notifyObservers();
	}
}