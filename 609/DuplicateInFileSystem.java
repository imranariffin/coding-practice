import java.util.HashMap;
import java.util.List;
import java.util.LinkedList;
import java.util.Iterator;

class DuplicateInFileSystem {
	public static List<List<String>> findDuplicate(String[] paths) {
		// hashmap: file content as key, list of files as value
		HashMap<String,List<String>> hm = new HashMap<String,List<String>>();
		List<List<String>> ret = new LinkedList<List<String>>();

		// populate the hashmap
		for (String path: paths) {
			String[] p = path.split(" ");
			String dir = null;
			for (int i=0; i<p.length; i++) {
				if (i == 0) { 
					dir = p[0];
				} else {
					String f = p[i];
					String content = f.substring(
						f.indexOf("(")+1, 
						f.indexOf(")"));
					String fulldir = dir + "/" + f.substring(
						0, 
						f.indexOf("("));
					if (hm.containsKey(content)) {
						((List<String>) hm.get(content)).add(fulldir);
					} else {
						List<String> ll = new LinkedList<String>();
						ll.add(fulldir);
						hm.put(content, ll);
					}
				}
			}
		}

		// collect only when files more than 1
		for (String content: hm.keySet()) {
			List<String> ll = hm.get(content);
			if (ll.size() > 1) {
				ret.add(ll);
			}
		}

		return ret;
	}

	public static void main(String[] args) {
		String[] paths = {
			"root/a 1.txt(abcd) 2.txt(efgh)", 
			"root/c 3.txt(abcd)", 
			"root/c/d 4.txt(efgh)", 
			"root 4.txt(efgh)"
		};
		List<List<String>> ret = findDuplicate(paths);
		for (List<String> ll: ret) {
			for (String s: ll) {
				System.out.format(s + ",");
			}
			System.out.format("\n");
		}
	}
}