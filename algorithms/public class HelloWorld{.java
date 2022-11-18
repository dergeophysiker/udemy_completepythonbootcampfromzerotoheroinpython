import java.util.Arrays;

public class HelloWorld{

     public static void main(String []args){
        System.out.println("Hello World");
        
        int[] args1 = {10, 20, 30, 40};
        
        int[] data = new int[args1.length];
		
		for (int i = 0; i < args1.length; i++)
		{
			int element = args1[i];
			data[i] = element;
			System.out.println(element);
		}
        
     }

     private static int[] threeWayMerge(int[] merged, int[] begin, int[] middle, int[] end)
     {
         int dataSize = begin.length + middle.length + end.length; //Total length
         merged = new int[dataSize]; //The final array where everything has been merged and sorted
         int bNum = 0; //Next element in the beginning array
         int mNum = 0; //Next element in the middle array
         int eNum = 0; //Next element in the ending array
         
         
         for (int i = 0; i < merged.length; i++)
         {
             boolean bDone = false; //Checks if all elements in beginning array are used
             boolean mDone = false; //Checks if all elements in middle array are used
             boolean eDone = false; //Checks if all elements in end array are used
             //Returns array after all elements have been sorted and used
             if (bDone == true && mDone == true && eDone == true)
             {
                 return merged;
                 
             }
             
             else
             {
                 /*
                  * Checks if the next element of the beginning array has the smallest value
                  * compared to the next elements of the other arrays.
                  */
                 if (begin[bNum] <= middle[mNum] && begin[bNum] <= end[eNum])
                 {
                     //Sets the next element of the merged array with that of the next beginning array element
                     merged[i] = begin[bNum];
                     if (bNum == begin.length - 1) //Checks if all elements of the beginning array were used
                     {
                         bDone = true;
                     }
                     else
                     {
                         bNum++; //Goes to the next element of the sorted beginning array
                     }	
                 }
             
                 /*
                  * Checks if the next element of the middle array has the smallest value
                  * compared to the next elements of the other arrays.
                  */
                 else if (middle[mNum] <= begin[bNum] && middle[mNum] <= end[eNum])
                 {
                     //Sets the next element of the merged array with that of the next middle array element
                     merged[i] = middle[mNum];
                     if (mNum == middle.length - 1)//Checks if all elements of the middle array were used
                     {
                         mDone = true;
                     }
                     else
                     {
                         mNum++; //Goes to the next element of the sorted middle array
                     }	
                 }
             
                 /*
                  * Checks if the next element of the end array has the smallest value
                  * compared to the next elements of the other arrays.
                  */
                 else if (end[eNum] <= begin[bNum] && end[eNum] <= middle[mNum])
                 {
                     //Sets the next element of the merged array with that of the next end array element
                     merged[i] = end[eNum];
                     if (eNum == end.length - 1) //Checks if all elements of the end array were used
                     {
                         eDone = true;
                     }
                     else
                     {
                         eNum++; //Goes to the next element of the sorted end array
                     }	
                 }
             }
         }
         
         bDone = false;
         mDone = false;
         eDone = false;
         System.out.println("Sorted:" + Arrays.toString(merged));
         
     }//end function


}//end class


