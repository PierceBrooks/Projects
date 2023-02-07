import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;
import java.util.Scanner;

public class CrudappJava {

    static class Employee{

        private int empno;
        private String ename;
        private int salary;

        Employee(int empno, String ename, int salary){
            this.empno = empno;
            this.ename = ename;
            this.salary = salary;

        }

        public int getEmpno(){
            return empno;
        }
        public int getSalary(){
            return salary;
        }
        public String getEname(){
            return ename;
        }
        public String toString(){
            return empno+" "+ename+" "+salary;
        }

    }

    class CRUDDemo{
        public static void main(String[] args) {

            Collection<Employee> c = new ArrayList<Employee>();
            Scanner s = new Scanner(System.in);
            Scanner s1 = new Scanner(System.in);
            int ch;
            do{
                System.out.println("1.INSERT");
                System.out.println("2.Display");
                System.out.println("3.SEARCH");
                System.out.println("4.DELETE");
                System.out.println("5.UPDATE");
                System.out.println("Enter Your Choice: ");
                ch = s.nextInt();

                switch (ch){
                    case 1:
                        System.out.print("Enter Employee Number: ");
                        int eno = s.nextInt();
                        System.out.print("Enter Employee Name: ");
                        String ename = s1.nextLine();
                        System.out.print("Enter Employee Salary: ");
                        int salary = s.nextInt();

                        c.add(new Employee(eno,ename,salary));
                    break;
                    case 2:
                        System.out.println("---------------------------------");
                        Iterator i = c.iterator();
                        while (i.hasNext()){
                            Employee e = (Employee) i.next();
                            System.out.println(e);
                        }
                        System.out.println("-----------------------------------");
                    break;
                    case 3:
                        boolean found = false;
                        System.out.println("Enter Employer Number :");
                        int empno = s.nextInt();
                        System.out.println("-------------------------------------");
                        Iterator<Employee> I = c.iterator();
                        while (I.hasNext()){
                            Employee e = I.next();
                            if(e.getEmpno()== empno){
                                System.out.println(e);
                                found = true;
                            }
                        }
                        if (!found){
                            System.out.println("Record Not Found");
                        }
                        System.out.println("-------------------------------------");
                    break;
                    case 4:
                        found = false;
                        System.out.println("Enter Employer Number to Delete: ");
                        empno =s.nextInt();
                        System.out.println("-------------------------------------");
                        i = c.iterator();
                        while (i.hasNext()){
                            Employee e = (Employee) i.next();
                            if(e.getEmpno()== empno) {
                                i.remove();
                                found = true;
                            }
                        }
                        if(!found){
                            System.out.println("Record Not Found");
                        }else{
                            System.out.println("Record is Deleted Successfully..!");
                        }
                        System.out.println("-------------------------------");
                }

            }while(ch!=0);
        }

    }
}
