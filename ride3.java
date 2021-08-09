class Person
    {
        
            String name;//instance variables should be initialised using constructors
            String address;
             long phone;
             String email; 
             public Person(String n,  String a, long p, String e)
             {
                name=n;
                address=a;
                phone=p;
                email=e;
             }
             public void getInfo()
             {
                //System.out.println("class name is : person");
                System.out.println("class name is: "+ getClass().getName());
                System.out.println("Person name is "+ name);
             }
        }

    class Student extends Person
        {
           
            final String status = "fresher";
            public Student(String n, String a, long p, String e)
            {
                super(n,a,p,e);
            }
            public void getInfo()
            {
                //System.out.println("class name is : person");
                System.out.println("class name is: "+ getClass().getName());
                System.out.println("student name is "+ name);
            }
        }
          


        class Employee extends Person
        {
            
            String office;
            double salary;
            String doj;
            public Employee(String n, String a, long p, String e, String o, double sal, String date)
            {
                    super(n,a,p,e);
                    office=o;
                    salary= sal;
                    doj=date;
            }
            public void getInfo()
            {
                //System.out.println("class name is : person");
                System.out.println("class name is: "+ getClass().getName());
                System.out.println("Employee name is "+ name);
            }
        }
           
        
        class Faculty extends Employee
        {
            String officehours;
            String rank;
            public Faculty(String n, String a, long p, String e, String o, double sal, String date, String oh,String r)
            {
                super(n,a,p,e,o,sal,date);
                officehours=oh;
                rank=r;
            }
            public void getInfo()
            {
                //System.out.println("class name is : person");
                System.out.println("class name is: "+ getClass().getName());
                System.out.println("Faculty name is "+ name);
            }
        }

           
            
        class Staff extends Employee
        {
            String title;
           // public Staff();
            public void getinfo(String n, String a, long p, String e, String o, double sal, String date,String t)
            {
                super(n,a,p,e,o,sal,date);
                title=t;
            }
            public void getInfo()
            {
               //System.out.println("class name is : person");
                System.out.println("class name is: "+ getClass().getName());
                System.out.println("Staff name is "+ name); 
            }
        }
          

class Testoverriding
{
    public static void main(String... dsfc) 
    {
        Person P=new Person("abc","bangalore",1234567890, "abc@xyz.com");
        P.getInfo();
        Student S=new Student("def","bangalore",1234567890, "abc@xyz.com");
        S.getInfo();
        Employee E=new Employee("ijk","bangalore",1234567890, "abc@xyz.com","Accounts",50000,"12/12/12");
        E.getInfo();
        Faculty F=new Faculty("lmn","bangalore",1234567890, "abc@xyz.com","Accounts",50000,"12/12/12","8:30 to 4:30","Professor");
        F.getInfo();
        Staff S=new Staff("opq","bangalore",1234567890, "abc@xyz.com","Accounts",50000,"12/12/12","Professor");
        S.getInfo();
    }
}