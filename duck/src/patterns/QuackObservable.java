package patterns;

public interface QuackObservable{
	public void registerObserver(Observer obs);
	public void notifyObservers();
}