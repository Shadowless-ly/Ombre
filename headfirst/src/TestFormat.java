import java.util.Formattable;
import java.util.Formatter;
import java.util.Calendar;
import java.util.Locale;

public class TestFormat {

    public static void main(String [] args){
        formatTimeAndDate();
        }

    private static void formatConversion(){
        System.out.println(String.format("'b':将参数格式化为boolean类型输出，'B'的效果相同,但结果中字母为大写。%b",false));
        System.out.println(String.format("'h':将参数格式化为散列输出，原理：Integer.toHexString(arg.hashCode())，'H'的效果相同,但结果中字母为大写。%h","ABC"));
        System.out.println(String.format("'s':将参数格式化为字符串输出，如果参数实现了 Formattable接口，则调用 formatTo方法。'S'的效果相同。%s",16));
        System.out.println(String.format("FormatImpl类实现了Formattable接口：%s",new FormatImpl()));
        System.out.println(String.format("'c':将参数格式化为Unicode字符，'C'的效果相同。%c",'A'));
        System.out.println(String.format("'d':将参数格式化为十进制整数。%d",11));
        System.out.println(String.format("'o':将参数格式化为八进制整数。%o",9));
        System.out.println(String.format("'x':将参数格式化为十六进制整数。%x",17));
        System.out.println(String.format("'e':将参数格式化为科学计数法的浮点数，'E'的效果相同。%E",10.000001));
        System.out.println(String.format("'f':将参数格式化为十进制浮点数。%f",10.000001));
        System.out.println(String.format("'g':根据具体情况，自动选择用普通表示方式还是科学计数法方式，'G'效果相同。10.01=%g",10.01));
        System.out.println(String.format("'g':根据具体情况，自动选择用普通表示方式还是科学计数法方式，'G'效果相同。10.00000000005=%g",10.00000000005));
        System.out.println(String.format("'a':结果被格式化为带有效位数和指数的十六进制浮点数，'A'效果相同,但结果中字母为大写。%a",10.1));
        System.out.println(String.format("'t':时间日期格式化前缀，会在后面讲述"));
        System.out.println(String.format("'%%':输出%%。%%"));
        System.out.println(String.format("'n'平台独立的行分隔符。System.getProperty(\"line.separator\")可以取得平台独立的行分隔符，但是用在format中间未免显得过于烦琐了%n已经换行"));

        System.out.println(String.format("Java提供了%1$s类用于格式化，我们可以使用%1$s的%2$s方法格式化字符串。", "java.util.Formatter", "format()"));
        }

    private static class FormatImpl implements Formattable {
        @Override
        public void formatTo(Formatter formatter, int flags, int width, int precision) {
            formatter.format("我是Formattable接口的实现类");
        }
    }
    private static void formatFlags() {
        System.out.println("'-':在最小宽度内左对齐，不可与\"用0填充\"同时使用。");
        System.out.println(String.format("设置最小宽度为8为，左对齐。%-8d:%-8d:%-8d%n", 1, 22, 99999999));
        System.out.println(String.format("'0':结果将用零来填充。设置最小宽度为8，%08d:%08d:%08d", 1, -22, 99999990));
        System.out.println(String.format("'+':结果总是包括一个符号。%+d:%+d:%+d", 1, -2, 0));
        System.out.println(String.format("' ':正值前加空格，负值前加负号。% d:% d:% d", 1, -2, 0));
        System.out.println(String.format("',':每3位数字之间用“，”分隔(只适用于fgG的转换)。%,d:%,d:%,d", 1, 100, 1000));
        System.out.println(String.format("'(':若参数是负数，则结果中不添加负号而是用圆括号把数字括起来(只适用于eEfgG的转换)。%(d:%(d", 1, -1));
        System.out.println(String.format("%s, %<s, %<s", "重复使用参数"));
    }

    private static void formatTime() {
        System.out.println("这是格式化时间相关的，具体输出跟你执行代码时间有关");
        Calendar calendar = Calendar.getInstance();
        System.out.println(String.format("'H':2位数24小时制，不足两位前面补0：%tH（范围：00-23）", calendar));
        System.out.println(String.format("'I':2位数12小时制，不足两位前面补0：%tI（范围：01-12）", calendar));
        System.out.println(String.format("'k':24小时制，不足两位不补0：%tk（范围：0-23）", calendar));
        System.out.println(String.format("'l':12小时制，不足两位不补0：%tl（范围：1-12）", calendar));
        System.out.println(String.format("'M':2位数的分钟，不足两位前面补0：%tM（范围：00-59）", calendar));
        System.out.println(String.format("'S':分钟中的秒，2位数，不足两位前面补0，60是支持闰秒的一个特殊值：%tS（范围：00-60）", calendar));
        System.out.println(String.format("'L':3位数的毫秒，不足三位前面补0：%tL（范围：000-999）", calendar));
        System.out.println(String.format("'N':9位数的微秒，不足九位前面补0：%tN（范围：000000000-999999999）", calendar));

        System.out.println(String.format("'p':输出本地化的上午下午，例如，Locale.US为am或pm，Locale.CHINA为上午或下午", calendar));
        System.out.println(String.format(Locale.US, "Local.US=%tp", calendar));
        System.out.println(String.format(Locale.CHINA, "Local.CHINA=%tp", calendar));
        System.out.println();

        System.out.println(String.format("'z':时区：%tz", calendar));
        System.out.println(String.format("'Z':时区缩写字符串：%tZ", calendar));
        System.out.println(String.format("'s':从1970-1-1 00:00到现在所经历的秒数：%ts", calendar));
        System.out.println(String.format("'Q':从1970-1-1 00:00到现在所经历的毫秒数：%tQ", calendar));
    }

    /**
     * 格式化日期
     */
    private static void formatDate() {
        System.out.println("这是格式化时间相关的，具体输出跟你执行代码时间有关");
        Calendar calendar = Calendar.getInstance();
        System.out.println(String.format("'B':本地化显示月份字符串，如：January、February"));
        System.out.println(String.format("'b':本地化显示月份字符串的缩写，如：Jan、Feb"));
        System.out.println(String.format("'h':本地化显示月份字符串的缩写，效果同'b'"));
        System.out.println(String.format(Locale.US, "Locale.US 月份=%1$tB，缩写=%1$tb", calendar));
        System.out.println(String.format(Locale.CHINA, "Locale.CHINA 月份=%1$tB，缩写=%1$tb", calendar));

        System.out.println(String.format("'A':本地化显示星期几字符串，如：Sunday、Monday"));
        System.out.println(String.format("'a':本地化显示星期几字符串的缩写，如：Sun、Mon"));
        System.out.println(String.format(Locale.US, "Locale.US 星期几=%1$tA，缩写=%1$ta", calendar));
        System.out.println(String.format(Locale.CHINA, "Locale.CHINA 星期几=%1$tA，缩写=%1$ta", calendar));

        System.out.println(String.format("'C':年份除以100的结果，显示两位数，不足两位前面补0：%tC（范围：00-99）", calendar));
        System.out.println(String.format("'Y':显示四位数的年份，格利高里历，即公历。不足四位前面补0：%tY", calendar));
        System.out.println(String.format("'y':显示年份的后两位：%ty（范围：00-99）", calendar));
        System.out.println(String.format("'j':显示当前公历年的天数：第%tj天（范围：001-366）", calendar));
        System.out.println(String.format("'m':显示当前月份：%tm月（范围：01-13？怎么会有13个月？）", calendar));
        System.out.println(String.format("'d':显示是当前月的第几天，不足两位前面补0：%1$tm月第%1$td天（范围：01-31）", calendar));
        System.out.println(String.format("'e':显示是当前月的第几天：%1$tm月第%1$te天（范围：1-31）", calendar));
    }

    /**
     * 格式化时间日期
     */
    private static void formatTimeAndDate() {
        System.out.println("这是格式化时间相关的，具体输出跟你执行代码时间有关");
        Calendar calendar = Calendar.getInstance();
        //%tH:%tM的缩写
        System.out.println(String.format("'R':将时间格式化为：HH:MM（24小时制）。输出：%tR", calendar));
        //%tH:%tM:%tS的缩写
        System.out.println(String.format("'T':将时间格式化为：HH:MM:SS（24小时制）。输出：%tT", calendar));
        //%tI:%tM:%tS %Tp的缩写，输出形如：
        System.out.println(String.format("'r':将时间格式化为：09:23:15 下午，跟设置的语言地区有关。输出：%tr", calendar));
        //%tm/%td/%ty的缩写，输出形如
        System.out.println(String.format("'D':将时间格式化为：10/19/16。输出：%tD", calendar));
        //%tY-%tm-%td，输出形如：
        System.out.println(String.format("'F':将时间格式化为：2016-10-19。输出：%tF", calendar));
        //%ta %tb %td %tT %tZ %tY，输出形如：Sun Jul 20 16:17:00 EDT 1969
        System.out.println(String.format("'c':将时间格式化为\"Sun Jul 20 16:17:00 EDT 1969\"。输出：%tc", calendar));
    }
}

