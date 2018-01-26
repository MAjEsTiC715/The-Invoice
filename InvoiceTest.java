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

public class InvoiceTest {

	public static void main(String[] args) {
		// create 4 objects and set values for each instance in the class Invoice
		Invoice invoice1 = new Invoice("5641", "Wedge", 4, 12.55);
		Invoice invoice2 = new Invoice("1234", "Golden Hammer", 2, 56.99);
		Invoice invoice3 = new Invoice("0012", "Pick axe", -5, 5.99);
		Invoice invoice4 = new Invoice("5000", "Apple", -4, -2.99);
		
		// print out the information using printf and format it using %s%d%.2f
		// access each object and use .get to obtain the information that has been stored
		// and calculated in class Invoice
		
		System.out.printf("Part number: %s\nDescription: %s\nQuantity: %d\nPrice: %.2f\n" +
				"Invoice amount: %.2f\n", invoice1.getNumber(), invoice1.getDesc(),
				invoice1.getQuantity(), invoice1.getPrice(), 
				invoice1.getInvoiceAmount(invoice1.getQuantity(), invoice1.getPrice()));
		
		System.out.printf("\nPart number: %s\nDescription: %s\nQuantity: %d\nPrice: %.2f\n" +
				"Invoice amount: %.2f\n", invoice2.getNumber(), invoice2.getDesc(),
				invoice2.getQuantity(), invoice2.getPrice(), 
				invoice2.getInvoiceAmount(invoice2.getQuantity(), invoice2.getPrice()));
		
		System.out.printf("\nPart number: %s\nDescription: %s\nQuantity: %d\nPrice: %.2f\n" +
				"Invoice amount: %.2f\n", invoice3.getNumber(), invoice3.getDesc(),
				invoice3.getQuantity(), invoice3.getPrice(), 
				invoice3.getInvoiceAmount(invoice3.getQuantity(), invoice3.getPrice()));
		
		System.out.printf("\nPart number: %s\nDescription: %s\nQuantity: %d\nPrice: %.2f\n" +
				"Invoice amount: %.2f\n", invoice4.getNumber(), invoice4.getDesc(),
				invoice4.getQuantity(), invoice4.getPrice(), 
				invoice4.getInvoiceAmount(invoice4.getQuantity(), invoice4.getPrice()));

	}

}
