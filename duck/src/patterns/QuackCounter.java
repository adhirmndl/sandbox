package patterns;

public class QuackCounter implements Quackable {

	Quackable duck;
	static int numOfQuacks;

	public QuackCounter(Quackable duck){
		this.duck = duck;
	}

	public void quack(){
		this.numOfQuacks += 1;
		this.duck.quack();
	}

	public static int getQuacks(){
		return numOfQuacks;
	}

	public void registerObserver(Observer obs){
		this.duck.registerObserver(obs);
	}

	public void notifyObservers(){
		this.duck.notifyObservers();
	}

}