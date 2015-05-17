package patterns;

import java.util.ArrayList;
import java.util.Iterator;

public class Flock implements Quackable{

	ArrayList quackers = new ArrayList();


	public void add(Quackable quacker){
		this.quackers.add(quacker);
	}

	public void quack(){
		Iterator iter = quackers.iterator();
		while (iter.hasNext()){
			Quackable quacker = (Quackable) iter.next();
			quacker.quack();
		}
	}

	public void registerObserver(Observer obs){
		Iterator iter = quackers.iterator();
		while (iter.hasNext()){
			Quackable quacker = (Quackable) iter.next();
			quacker.registerObserver(obs);
		}

	}

	public void notifyObservers(){
		Iterator iter = quackers.iterator();
		while (iter.hasNext()){
			Quackable quacker = (Quackable) iter.next();
			quacker.notifyObservers();
		}
	}

}