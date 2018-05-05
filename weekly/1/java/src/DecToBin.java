class DecToBin{
    public static void main(String[] args) {
//        String a = oct2Bin(8);
//        System.out.println(a);
        String a = new StringBuffer(oct2Bin(-8)).reverse().toString();
        System.out.println(a);
//        }
    }
    public static String oct2Bin(int a){
        int[] bin = new int[32];
        String flag;
        String res = "";
        int i = 0;
        int d;
        if (a < 0){
            flag = "-";
            d = -a;
        }
        else{
            flag="";
            d = a;
        }


        while (d >= 2){
            res = res + d % 2;
            d = d / 2;
            if (d < 2){
                res = res + 1;
            }
            i ++;
        }
        res = res + flag;
        return res;
    }
}