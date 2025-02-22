class MusicalInstrument {
    String play() {
        return "Sound";
    }
}

class Guitar extends MusicalInstrument {
    @Override
    String play() {
        return "Guitar sound";
    }
}

class Drum extends MusicalInstrument {
    @Override
    String play() {
        return "Drum beat";
    }
}

class InstrumentFactory {
    MusicalInstrument createInstrument() {
        return new MusicalInstrument();
    }
}

class GuitarFactory extends InstrumentFactory {
    // Overriding the method with a covariant return type
    @Override
    Guitar createInstrument() {
        return new Guitar();
    }
}

class DrumFactory extends InstrumentFactory {
    // Overriding the method with a covariant return type
    @Override
    Drum createInstrument() {
        return new Drum();
    }
}

public class Main {
    public static void main(String[] args) {
        // Polymorphism
        MusicalInstrument guitar = new Guitar();
        MusicalInstrument drum = new Drum();
        System.out.println(guitar.play()); // Guitar sound
        System.out.println(drum.play()); // Drum beat

        // Covariant
        InstrumentFactory guitarFactory = new GuitarFactory();
        InstrumentFactory drumFactory = new DrumFactory();
        MusicalInstrument myGuitar = guitarFactory.createInstrument();
        MusicalInstrument myDrum = drumFactory.createInstrument();
        System.out.println(myGuitar.play()); // Guitar sound
        System.out.println(myDrum.play()); // Drum beat
    }
}
