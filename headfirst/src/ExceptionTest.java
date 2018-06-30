public class ExceptionTest {
    public static void main(String[] args) {
        ExpTest exptest = new ExpTest();
        try{
            exptest.toInt(11);
        } catch (TypeError e){
            String a = e.getMessage();
            System.out.println(a);
        } finally{
        System.out.println("we made it!");
        }
    }
}


class ExpTest {
    public static void toInt(int num) throws TypeError {
        if (num <= 10) {
            System.out.println("num is below ten!");
        }
        else{
            throw new TypeError();
        }
    }


}

class TypeError extends Exception {
    TypeError(){
        super();
    }

    public String getMessage(){
        System.out.println(String.format("num is more than ten!"));
        return "failed";
    }
}