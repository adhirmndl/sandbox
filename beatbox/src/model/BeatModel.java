package model;

import java.util.*;
import javax.sound.midi.*;

import util.BeatObserver;
import util.BPMObserver;

public class BeatModel implements BeatModelInterface, MetaEventListener {

	Sequencer sequencer;
	ArrayList beatObservers = new ArrayList();
	ArrayList bpmObservers  = new ArrayList();
	int bpm = 90;

	Sequence sequence;
	Track track;

	public void initialize(){
		this.setupMidi();
		buildTrackAndStart();
	}

	public void on(){
		this.sequencer.start();
		setBPM(this.bpm);
	}

	public void off(){
		setBPM(0);
		this.sequencer.stop();
	}

	public void setBPM(int bpm){
		this.bpm = bpm;
		this.sequencer.setTempoInBPM(this.getBPM());
		notifyBPMObservers();
	}

	public int getBPM(){
		return this.bpm;
	}

	public void beatEvent(){
		notifyBeatObservers();
	}

	public void registerObserver(BeatObserver o){
		this.beatObservers.add(o);
	}

	public void notifyBeatObservers(){
		Iterator iter = beatObservers.iterator();
		while(iter.hasNext()){
			BeatObserver bo = (BeatObserver) iter.next();
			bo.updateBeat();
		}
	}

	public void removeObserver(BeatObserver o){
		this.beatObservers.remove(o);
	}

	public void registerObserver(BPMObserver o){
		this.bpmObservers.add(o);
	}

	public void notifyBPMObservers(){
		Iterator iter = bpmObservers.iterator();
		while(iter.hasNext()){
			BeatObserver bo = (BeatObserver) iter.next();
			bo.updateBeat();
		}
	}

	public void removeObserver(BPMObserver o){
		this.beatObservers.remove(o);
	}

	public void meta(MetaMessage message){
		if (message.getType() == 47){
			beatEvent();
			sequencer.start();
			setBPM(getBPM());
		}
	}

	public void setupMidi(){
		try{
			this.sequencer = MidiSystem.getSequencer();
			this.sequencer.open();
			this.sequencer.addMetaEventListener(this);
			this.sequence = new Sequence(Sequence.PPQ, 4);
			track = sequence.createTrack();
			sequencer.setTempoInBPM(this.getBPM());
		} catch (Exception e){
			e.printStackTrace();
		}
	}

	public void buildTrackAndStart(){
		int[] trackList = {35, 0, 46, 0};
    
        sequence.deleteTrack(null);
        track = sequence.createTrack();

      	makeTracks(trackList);
		track.add(makeEvent(192,9,1,0,4));      
	 	try {
			sequencer.setSequence(sequence);                    
		} catch(Exception e) {
			e.printStackTrace();
		}
	}

	public void makeTracks(int[] list) {        
       
       for (int i = 0; i < list.length; i++) {
          int key = list[i];

          if (key != 0) {
             track.add(makeEvent(144,9,key, 100, i));
             track.add(makeEvent(128,9,key, 100, i+1));
          }
       }
    }
        
    public  MidiEvent makeEvent(int comd, int chan, int one, int two, int tick) {
        MidiEvent event = null;
        try {
            ShortMessage a = new ShortMessage();
            a.setMessage(comd, chan, one, two);
            event = new MidiEvent(a, tick);
            
        } catch(Exception e) {
			e.printStackTrace(); 
		}
        return event;
    }

}