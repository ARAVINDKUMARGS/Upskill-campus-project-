// BankingInformationSystem.java
import java.util.*;

public class BankingInformationSystem {
    static Scanner sc = new Scanner(System.in);
    static Map<Integer, Double> accounts = new HashMap<>();
    static int nextAccountNo = 1001;

    public static void main(String[] args) {
        while (true) {
            System.out.println("\n--- Banking Information System ---");
            System.out.println("1. Open New Account");
            System.out.println("2. Deposit");
            System.out.println("3. Withdraw");
            System.out.println("4. Check Balance");
            System.out.println("5. Exit");
            System.out.print("Choose an option: ");
            int choice = sc.nextInt();

            switch (choice) {
                case 1:
                    openAccount();
                    break;
                case 2:
                    deposit();
                    break;
                case 3:
                    withdraw();
                    break;
                case 4:
                    checkBalance();
                    break;
                case 5:
                    System.out.println("Thank you for using the system!");
                    return;
                default:
                    System.out.println("Invalid option.");
            }
        }
    }

    static void openAccount() {
        int accNo = nextAccountNo++;
        accounts.put(accNo, 0.0);
        System.out.println("Account opened successfully. Account No: " + accNo);
    }

    static void deposit() {
        System.out.print("Enter account number: ");
        int accNo = sc.nextInt();
        if (accounts.containsKey(accNo)) {
            System.out.print("Enter amount to deposit: ");
            double amount = sc.nextDouble();
            accounts.put(accNo, accounts.get(accNo) + amount);
            System.out.println("Deposit successful.");
        } else {
            System.out.println("Account not found.");
        }
    }

    static void withdraw() {
        System.out.print("Enter account number: ");
        int accNo = sc.nextInt();
        if (accounts.containsKey(accNo)) {
            System.out.print("Enter amount to withdraw: ");
            double amount = sc.nextDouble();
            double balance = accounts.get(accNo);
            if (amount <= balance) {
                accounts.put(accNo, balance - amount);
                System.out.println("Withdrawal successful.");
            } else {
                System.out.println("Insufficient balance.");
            }
        } else {
            System.out.println("Account not found.");
        }
    }

    static void checkBalance() {
        System.out.print("Enter account number: ");
        int accNo = sc.nextInt();
        if (accounts.containsKey(accNo)) {
            System.out.println("Balance: ₹" + accounts.get(accNo));
        } else {
            System.out.println("Account not found.");
        }
    }
          }
