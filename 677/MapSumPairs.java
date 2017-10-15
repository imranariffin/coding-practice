class MapSum {
    Node node;
    /** Initialize your data structure here. */
    public MapSum() {
        node = new Node();
    }
    class Node {
        public Map<Character,Node> map;
        public int val;
        public boolean black;
        public Node() {
            map = new HashMap<>();
            black = false;
        }
        public Node(int _val) {
            map = new HashMap<>();
            val = _val;
            black = true;
        }
    }
    
    public void insert(String key, int val) {
        Node cur = node;
        for (char c: key.toCharArray()) {
            if (!cur.map.containsKey(c)) {
                Node child = new Node();
                cur.map.put(c, child);
            }
            cur = cur.map.get(c);
        }
        cur.black = true;
        cur.val = val;
    }
    
    public int sum(String prefix) {
        Node cur = get(prefix);
        // System.out.println(cur.black);
//         dfs
        return _sum(cur);
    }
    
    private int _sum(Node cur) {
        if (cur == null) {
            return 0;
        }
        int ret = 0;
        if (cur.black) {
            ret += cur.val;
        }
        for (char c: cur.map.keySet()) {
            // System.out.println(c);
            if (cur.map.containsKey(c)) {
                ret += _sum(cur.map.get(c));
            }
        }
        return ret;
    }
    
    private Node get(String prefix) {
        Node cur = node;
        for (char c: prefix.toCharArray()) {
            if (!cur.map.containsKey(c)) {
                return null;
            }
            cur = cur.map.get(c);
        }
        return cur;
    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */
