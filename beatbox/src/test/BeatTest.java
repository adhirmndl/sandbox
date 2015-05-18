package test;

import model.BeatModelInterface;
import model.BeatModel;
import controller.ControllerInterface;
import controller.BeatController;

public class BeatTest {

	public static void main(String[] args){
		BeatModelInterface model = new BeatModel();
		ControllerInterface controller = new BeatController(model);
	}

}