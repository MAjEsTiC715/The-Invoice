//Documentation
/*1. Create a class called Invoice that a hardware store might use to represent 
 * an invoice for an item sold at the store. An Invoice should include four pieces 
 * of information as instance variables—a part number (type String), a part 
 * description (type String), a quantity of the item being purchased (type int) 
 * and a price per item (double). Your class should have a constructor that 
 * initializes the four instance variables. Provide a set and a get method for 
 * each instance variable. In addition, provide a method named getInvoiceAmount 
 * that calculates the invoice amount (i.e., multiplies the quantity by the 
 * price per item), then returns the amount as a double value. If the quantity 
 * is not positive, it should be set to 0. If the price per item is not positive, 
 * it should be set to 0.0. Write a test application named InvoiceTest that 
 * demonstrates class Invoice’s capabilities. */

public class Invoice {
	
	private String number; // instance variable
	private String desc; // instance variable
	private int quantity; // instance variable
	private double price; // instance variable

	// constructor initializes number, desc, quantity, and price with parameter name
	public Invoice(String number, String desc, int quantity, double price)
	{
		this.number = number;
		this.desc = desc;
		this.quantity = quantity;
		this.price = price;
	}
	// method to set the number
	public void setNumber(String number) 
	{
		this.number = number;
	}
	// method to set the desc
	public void setDesc(String desc) 
	{
		this.desc = desc;
	}
	// method to set the quantity
	public void setQuantity(int quantity) 
	{
		this.quantity = quantity;
	}
	// method to set the price
	public void setPrice(double price) 
	{
		this.price = price;
	}
	// method that calculates the Invoice amount 
	public double getInvoiceAmount(int quantity, double price)
	{
		double invoiceAmount = quantity * price;
		
		return invoiceAmount; // return the solution invoiceAmount
	}
	// method to retrieve the number
	public String getNumber() 
	{
		return number;
	}
	// method to retrieve the desc
	public String getDesc() 
	{
		return desc;
	}
	// method to retrieve the quantity
	public int getQuantity() 
	{ //the if statement determines if quantity is above 0
		if ( quantity > 0 )
		{
		return quantity; //returns the number if so
		}
		return 0; // returns 0 if not
	}
	// method to retrieve the price
	public double getPrice() 
	{ //the if statement determines if quantity is above 0
		if ( price > 0 )
		{
		return price; //returns the number if so
		}
		return 0.0; // returns 0 if not
	}

}
