class pe34
{
	public static void main(String args[])
	{
		int factorial[]=new int[10],n=3,su,s=0,dup;
		factorial[0]=1;
		for(int i=1;i<10;i++)
			factorial[i]=factorial[i-1]*i;
		while(true)
		{
			dup=n;
			su=0;
			while(dup>0)
			{
				su+=factorial[dup%10];
				dup/=10;
			}
			if(su==n)
			{
				s+=n;
				System.out.println(n+" "+s);
			}
			n++;
		}
	}
}