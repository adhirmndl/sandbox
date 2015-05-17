package patterns;

import other.Goose;

public class GooseAdapter implements Quackable{

	Goose goose;
	Observable observable;

	public GooseAdapter(Goose goose){
		this.goose = goose;
		this.observable = new Observable(this);
	}

	public void quack(){
		this.goose.honk();
		notifyObservers();
	}

	public void registerObserver(Observer obs){
		this.observable.registerObserver(obs);
	}

	public void notifyObservers(){
		this.observable.notifyObservers();
	}
}