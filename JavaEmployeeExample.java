// Java application example over adding emoployees into your system. :D



import java.util.Scanner;

class Employee{
   
   int id;
   String name;
   int age;
   int salary;
   
   void GetData() // Defining GetData()
   {

      Scanner sc = new Scanner(System.in);

      System.out.print("Enter Employee ID: ");    
      id = Integer.parseInt(sc.nextLine());
   
      System.out.print("Enter Employee name: ");
      name = sc.nextLine();
   
      System.out.print("Enter Employee age: ");
      age = Integer.parseInt(sc.nextLine());
   
      System.out.print("Enter Employee salary: ");
      salary = Integer.parseInt(sc.nextLine());

   }

   void PutData() // Defining PutData()
   {
   
      System.out.print("Employee ID: " + id);
   
      System.out.print("Employee Name: " + name);
    
      System.out.print("Employee age: " + age);
     
      System.out.print("Employee salary: " + salary);
   
   }

   public static void main(String args[])
   {
   

      Employee[] Emp = new Employee[3];

      int i;

      for(i=0;i<3;i++)
         Emp[i] = new Employee();       // Allocating memory to each object

      for(i=0;i<3;i++)

      {

         System.out.print("Enter details of " + (i+1) + "Employee ");

         Emp[i].GetData();

      }

         System.out.print("Details of employees: ");

         for(i=0;i<3;i++)

         Emp[i].PutData();
      
   }

}