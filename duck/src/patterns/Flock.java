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
}