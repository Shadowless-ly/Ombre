import java.util.Calendar;

public class TestCalendar {
    public static void main (String[] args) {
        Calendar cal = Calendar.getInstance();
        System.out.println(cal.getClass());
        cal.set(2008, 6, 9, 22,38);
        long day1 = cal.getTimeInMillis();
        System.out.println(day1);
        day1 += 1000 * 60 * 60;
        cal.setTimeInMillis(day1);
        System.out.println("new hour " + cal.get(cal.HOUR_OF_DAY));
        cal.add(cal.DATE, 35);
        System.out.println("add 35 days " + cal.getTime());
        cal.roll(cal.DATE, 35);
        System.out.println("roll 35 days " + cal.getTime());
        cal.set(cal.DATE, 1);
        System.out.println("set to 1 " + cal.getTime());
        }
}
