public static void main(String[] args) {
    //create the ContactsManager object
    ContactsManager myContactsManager = new ContactsManager();
    //Create new contact object for James
    Contact friendJames = new Contact();
    //Set fields
    friendJames.name = "James";
    friendJames.phoneNumber = "0782900245";
    //Add James Contact to ContactsManager
    myContactsManager.addContact(friendJames);
    //create a new contact object for jesca
    Contact friendJesca = new Contact();
    //set fields
    friendJesca.name = "Jesca";
    friendJesca.phoneNumber = "0783911356";
    //add Jesca Contact to ContactsManager
    myContactsManager.addContact(friendJesca);

    //search for a contact and dispaly their phone number
    Contact result = myContactsManager.searchContact("Jesca");
    System.out.println(result.phoneNumber);
}

