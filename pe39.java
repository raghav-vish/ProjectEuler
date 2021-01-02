class pe34
{
	public static void main(String args[])
	{
		int sol,maxsol=0,maxp=0,a,b,c,p;
		for(p=1;p<=1000;p++)
		{
			sol=0;
			for(a=1;a<p;a++)
			{
				for(b=a+1;b<p;b++)
				{
					c=p-a-b;
					if(c>b && a+b>c && b+c>a && a+c>b && a*a+b*b==c*c)
						sol++;
				}
			}
			if(sol>maxsol)
			{
				maxsol=sol;
				maxp=p;
			}
		}
		System.out.print(maxp);
	}
}