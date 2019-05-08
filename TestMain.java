public class TestMain
{
    //@param args
    public static void main(String[] args)
    {
        //TODO Auto-generated method stub
        int n=args.length;    //获取参数数量
        System.out.println("一共有 "+n+" 个参数");
        if(n>0)
        {   
            //判断参数个数是否大于0
            for(int i=0;i<n;i++)
            {
                System.out.println(args[i]);
            }
        }
    }
}