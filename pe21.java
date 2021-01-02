class pe21
{
	static long sof(long n)
	{
		long f=1;
		for(long i=2;i<n;i++)
		{
			if(n%i==0)
				f+=i;
		}
		return f;
	}

	public static void main(String args[])
	{
		long sum=0,f[]=new long[10000];
		for(long i=0;i<10000;i++)
			f[i]=sof(i);
		for(long i=2;i<10000;i++)
		{
			for(long j=i+1;j<10000;j++)
				if(f[i]==f[j])
					sum+=i+j;
		}
		System.out.println(sum);
	}
}