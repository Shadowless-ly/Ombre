import javax.swing.*;
import javax.swing.plaf.basic.BasicOptionPaneUI;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.*;

public class SimpleGui1B implements ActionListener {
    JButton button;
    public static void main(String[] args) {
        SimpleGui1B gui = new SimpleGui1B();
        gui.go();
    }

    public void go() {
        JFrame frame = new JFrame();
        button = new JButton("click me");
        button.addActionListener(this);

        MyDrawPanel draw = new MyDrawPanel();

        frame.getContentPane().add(draw);

//        frame.getContentPane().add(button);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 300);
        frame.setVisible(true);

    }

    public void actionPerformed(ActionEvent event) {
        button.setText("I've been clicked!");
    }
}

class MyDrawPanel extends JPanel {
    public void paintComponent(Graphics g) {
        // 可以将g想象为绘图装置
//        g.setColor(Color.orange);
//        g.fillRect(20, 50, 100, 100);

        // 显示图片
//        Image image = new ImageIcon("firstblog.png").getImage();
//        g.drawImage(image, 3, 4, this);

        // 画随机色彩的圆圈
        // 前两个时起点坐标，后面为宽度，高度,以默认颜色填充
        g.fillRect(0, 0, this.getWidth(), this.getHeight());

        int red=0;
        int green=0;
        int blue=0;
        while (red != 123 || blue != 123 || green != 123) {
            red = (int) (Math.random() * 255);
            green = (int) (Math.random() * 255);
            blue = (int) (Math.random() * 255);
        }
        String r = Integer.toString(red);
        String gr = Integer.toString(green);
        String b = Integer.toString(blue);
        System.out.println(r+gr+b);
        Color randomColor = new Color(red, green, blue);
        g.setColor(randomColor);
        g.fillOval(70, 70, 100, 100);


    }
}