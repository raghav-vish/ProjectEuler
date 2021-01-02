class pe14
{
	static long nof(long n)
	{
		long f=0;
		for(long i=1;i<n/2;i++)
		{
			if(n%i==0)
				f+=2;
			if(i*1.0==n*1.0/i)
				f--;
		}
		return f;
	}

	public static void main(String args[])
	{
		long maxsteps=0,steps=0,maxn=0,n,dup;
		for(n=2;n<1000000;n++)
		{
			dup=n;
			steps=0;
			while(dup!=1)
			{
				steps++;
				if(dup%2==0)
					dup/=2;
				else
				{
					dup=3*dup+1;
					dup/=2;
					steps++;
				}
			}
			if(steps>maxsteps)
			{
				maxsteps=steps;
				maxn=n;
			}
		}
		System.out.println(maxn);
	}
}