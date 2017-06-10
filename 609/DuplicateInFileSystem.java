import java.util.HashMap;
import java.util.List;
import java.util.LinkedList;
import java.util.Iterator;

class DuplicateInFileSystem {
	public static List<List<String>> findDuplicate(String[] paths) {
		HashMap<String,List<String>> hm = new HashMap<String,List<String>>();
		List<List<String>> ret = new LinkedList<List<String>>();

		for (String path: paths) {
			String[] p = path.split(" ");
			String dir = null;
			for (int i=0; i<p.length; i++) {
				if (i == 0) { 
					dir = p[0];
				} else {
					String file = p[i];
					String content = file.substring(file.indexOf("(")+1, file.indexOf(")"));
					if (hm.containsKey(content)) {
						((List<String>) hm.get(content)).add(dir + "/" + file.substring(0, file.indexOf("(")));
					} else {
						List<String> ll = new LinkedList<String>();
						ll.add(dir + "/" + file.substring(0, file.indexOf("(")));
						hm.put(content, ll);
					}
				}
			}
		}

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