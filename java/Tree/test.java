public class test {
    public static void main(String[] args) {
        simpleTree tree = new simpleTree();
        tree.insert(50);
        tree.insert(30);
        tree.insert(45);
        tree.insert(25);
        tree.insert(60);
        tree.insert(80);
        tree.insert(75);
        // tree.preorder();
        tree.inorder();
        // tree.postorder();
        tree.delete(60);
        tree.inorder();
    }
}