package ducks;

import patterns.Quackable;

public class DuckCall implements Quackable {
	public void quack(){
		System.out.println("Kwak");
	}
}