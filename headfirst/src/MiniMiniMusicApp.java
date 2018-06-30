import javax.sound.midi.*;


public class MiniMiniMusicApp {
    public static void main(String[] args){
        // 实例化播放器，调用其播放方法
        MiniMiniMusicApp mini = new MiniMiniMusicApp();
        if (args.length < 2) {
            System.out.println("Don't forget the instrument and note args");
            } else {
            int intrument = Integer.parseInt(args[0]);
            int note = Integer.parseInt(args[1]);
            mini.play(intrument, note);
            }
        }


    public void play(int instrument, int note){
        try{
            // 使用MidiSystem的getSequencer取得一个播放器(Sequencer)对象
            Sequencer player = MidiSystem.getSequencer();
            // 打开播放器
            player.open();
            // 实例化一个Sequence，相当于单曲CD
            Sequence seq = new Sequence(Sequence.PPQ, 4);
            // 使用Sequence的createTrack方法创建一个Track实例,Track相当于CD上的歌曲
            Track track = seq.createTrack();

            MidiEvent event = null;

            /** MidiEvent相当于音符,组合乐曲的指令，一连串的MidiEvent好像时乐谱一样
             *  需要指定某个音符何时播放(NOTE ON),何时停止(NOTE OFF)
             *  MIDI指令会放在Message对象中，MidiEvent时由Message加上发音的时机组成
             *  在MidiEvent中有”开始播放C“的指令，同时也有“于第四节拍执行指令”的信息
             */

            // 设置乐器
            ShortMessage first = new ShortMessage();
            first.setMessage(192, 1 , instrument, 0);
            MidiEvent changeInstrument = new MidiEvent(first, 1);
            track.add(changeInstrument);


            // 创建Message
            ShortMessage a = new ShortMessage();
            /** 传入指令
             *  144代表“NOTE ON”，1为频道(不同乐器)，44为音符(0-127)，100为音道(多大的声音)
             */
            a.setMessage(144, 1, note, 100);
            // 用message创建MidiEvent
            MidiEvent noteOn = new MidiEvent(a, 14);
            // 将MidiEvent加入Track中
            track.add(noteOn);

            ShortMessage b = new ShortMessage();
            b.setMessage(128, 1, note, 100);
            MidiEvent noteOff = new MidiEvent(b, 16);
            track.add(noteOff);
            // 设置播放器播放乐曲为seq（Sequence）
            player.setSequence(seq);
            // Begin play
            player.start();

        } catch (MidiUnavailableException ex){
            ex.printStackTrace();
        } catch (InvalidMidiDataException ex){
            ex.printStackTrace();
        }
    }
}
