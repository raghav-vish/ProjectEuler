class pe23
{
	public static void main(String args[])
	{
		long i,f,j,d,k=0,abundant[]=new long[21812];
		for(i=12;i<21824;i++)
		{
			f=1;
			for(j=2;j<i/2;j++)
			{
				if(i%j==0)
				{
					f+=j;
					d=i/j;
					if(j!=d)
						f+=d;
					if(f>i)
					{
						abundant[(long)k++]=i;
						break;
					}
				}
			}
		}
	}
}