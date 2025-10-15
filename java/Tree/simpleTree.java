public class simpleTree {
    Node root = null;
    int count = 0;

    simpleTree() {

    }

    class Node {
        int data;
        Node left = null;
        Node right = null;

        public Node(int ele) {
            data = ele;
        }
    }

    public void insert(int ele) {
        root =_insert(ele, root);
    }
    
    private Node _insert(int ele, Node node) {
        if (node == null) {
            return new Node(ele);
        }
        if (ele < node.data) {
            node.left = _insert(ele, node.left);
        } else if (ele > node.data) {
            node.right = _insert(ele, node.right);
        }
        return node;
    }
    
    public void delete(int key){
        _delete_(root, key);
    }

    private Node _delete_(Node node , int key){
        if (node == null){
            return node;
        }

        if(node.data>key){
            node.left = _delete_(node.left, key);
        } else if(node.data<key){
            node.right = _delete_(node.right, key);
        }
        else{
            if(node.left == null){
                return node.right;
            }else if(node.right == null){
                return node.left;
            }else{
                Node succ = getMin(node.right);
                node.data = succ.data;
                node.right = _delete_(node.right, succ.data);
            }
        }
        return node;
    }

    private Node getMin(Node node){
        Node temp = node;
        while (temp.left != null) {
            temp = temp.left;
        }
        return temp;
    }

    public void inorder() {
        _inorder(root);
        System.out.println();
    }

    private void _inorder( Node node) {
        if (node!=null){
            _inorder(node.left);
            System.out.print(node.data+" ");
            _inorder(node.right);
        }
    }

    public void preorder() {
        _preorder(root);
        System.out.println();
    }

    private void _preorder( Node node) {
        if (node!=null){
            System.out.print(node.data+" ");
            _preorder(node.left);
            _preorder(node.right);
        }
    }

    public void postorder() {
        _postorder(root);
        System.out.println();
    }

    private void _postorder( Node node) {
        if (node!=null){
            _postorder(node.left);
            _postorder(node.right);
            System.out.print(node.data+" ");
        }
    }
}