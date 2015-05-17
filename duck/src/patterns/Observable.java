package patterns;

import java.util.ArrayList;
import java.util.Iterator;

public class Observable implements QuackObservable {

	ArrayList observers = new ArrayList();

	QuackObservable duck;

	public Observable(QuackObservable duck){
		this.duck = duck;
	}

	public void registerObserver(Observer obs){
		observers.add(obs);
	}

	public void notifyObservers(){
		Iterator iter = observers.iterator();
		while(iter.hasNext()){
			Observer obs = (Observer) iter.next();
			obs.update(duck);
		}
	}
}