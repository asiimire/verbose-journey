//this class is responsible for adding and searching for contacts
public class ContactsManager {
    public static void main(String[] args) {
        //Fields
        Contact [] myFriends;
        int friendsCount;
        //Constructor:
        ContactsManager(){
            this.friendsCount = 0;
            this.myFriends = new Contact[500];
            //friendsCount starts from 0 and will increment everytime we add a new contact later
            //the Contact array myFriends (justlike any other array) needs to be initialized using the 'new' keyword and we chose to reserve enough space in the  array to store up to 500 contacts.

            //Methods
            //the first method addContact adds a Contact object to the Contact array myFriends
            //addContact takes a Contact object as an input parameter, and uses the friendsCount value to fill that slot in the array with the contact that was passed into the method
            //then, since we need to move that counter to the point to the following slot in the array,we increment friendsCount using the increment operation ++
            void addContact(Contact contact){
                myFriends[friendsCount] = contact;
                friendsCount++;
            }

            //next method is searchContact, it will search through the array using a name String and return a Contact object once a match is found
            Contact searchContact(String searchName){
                for (int i=0; i<friendsCount;i++){
                    if (myFriends[i].name.equals(searchName)){
                        return myFriends[i];
                    }
                }
                return null;
            }
        }
    }

}
