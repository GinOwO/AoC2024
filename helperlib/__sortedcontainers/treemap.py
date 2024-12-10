from typing import TypeVar, Generic, Callable, Optional, List
import operator

K = TypeVar("K")
V = TypeVar("V")


class Node:
    def __init__(self, key: K, value: V, color: bool = True) -> None:
        self.key: K = key
        self.value: V = value
        self.color: bool = color
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.parent: Optional[Node] = None

    def __repr__(self) -> str:
        return f"{self.key}: {self.value}"


class TreeMap(Generic[K, V]):
    def __init__(
        self,
        v_default: Callable[[], V] = None,
        cmp: Callable[[K, K], bool] = operator.lt,
    ) -> None:
        self.root: Optional[Node] = None
        self.cmp: Callable[[K, K], bool] = cmp
        self.v_default = v_default

    def __len__(self) -> int:
        def _count_nodes(node: Optional[Node]) -> int:
            if node is None:
                return 0
            return 1 + _count_nodes(node.left) + _count_nodes(node.right)

        return _count_nodes(self.root)

    def count(self, key: K) -> int:
        return 1 if self.search_node(key) is not None else 0

    def _is_red(self, node: Optional[Node]) -> bool:
        if node is None:
            return False
        return node.color

    def _rotate_left(self, node: Node) -> None:
        right_child = node.right
        node.right = right_child.left
        if right_child.left is not None:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def _rotate_right(self, node: Node) -> None:
        left_child = node.left
        node.left = left_child.right
        if left_child.right is not None:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

    def _flip_colors(self, node: Node) -> None:
        node.color = not node.color
        node.left.color = not node.left.color
        node.right.color = not node.right.color

    def _insert_fixup(self, node: Node) -> None:
        while node != self.root and self._is_red(node.parent):
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if self._is_red(uncle):
                    self._flip_colors(node.parent.parent)
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._rotate_left(node)
                    node.parent.color = False
                    node.parent.parent.color = True
                    self._rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if self._is_red(uncle):
                    self._flip_colors(node.parent.parent)
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)
                    node.parent.color = False
                    node.parent.parent.color = True
                    self._rotate_left(node.parent.parent)
        self.root.color = False

    def insert(self, key: K, value: V) -> None:
        new_node = Node(key, value, color=True)
        parent = None
        current = self.root
        while current is not None:
            parent = current
            if self.cmp(key, current.key):
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif self.cmp(key, parent.key):
            parent.left = new_node
        else:
            parent.right = new_node

        self._insert_fixup(new_node)

    def _transplant(self, u: Node, v: Optional[Node]) -> None:
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def _min_node(self, node: Node) -> Node:
        while node.left is not None:
            node = node.left
        return node

    def _delete_fixup(self, node: Optional[Node]) -> None:
        while node != self.root and not self._is_red(node):
            if node == node.parent.left:
                sibling = node.parent.right
                if self._is_red(sibling):
                    sibling.color = False
                    node.parent.color = True
                    self._rotate_left(node.parent)
                    sibling = node.parent.right
                if not self._is_red(sibling.left) and not self._is_red(sibling.right):
                    sibling.color = True
                    node = node.parent
                else:
                    if not self._is_red(sibling.right):
                        sibling.left.color = False
                        sibling.color = True
                        self._rotate_right(sibling)
                        sibling = node.parent.right
                    sibling.color = node.parent.color
                    node.parent.color = False
                    sibling.right.color = False
                    self._rotate_left(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if self._is_red(sibling):
                    sibling.color = False
                    node.parent.color = True
                    self._rotate_right(node.parent)
                    sibling = node.parent.left
                if not self._is_red(sibling.right) and not self._is_red(sibling.left):
                    sibling.color = True
                    node = node.parent
                else:
                    if not self._is_red(sibling.left):
                        sibling.right.color = False
                        sibling.color = True
                        self._rotate_left(sibling)
                        sibling = node.parent.left
                    sibling.color = node.parent.color
                    node.parent.color = False
                    sibling.left.color = False
                    self._rotate_right(node.parent)
                    node = self.root
        node.color = False

    def delete(self, key: K) -> None:
        node = self.search_node(key)
        if node is None:
            return

        y = node
        y_original_color = y.color
        if node.left is None:
            x = node.right
            self._transplant(node, node.right)
        elif node.right is None:
            x = node.left
            self._transplant(node, node.left)
        else:
            y = self._min_node(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self._transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color

        if y_original_color == False:
            self._delete_fixup(x)

    def search_node(self, key: K) -> Optional[Node]:
        current = self.root
        while current is not None:
            if key == current.key:
                return current
            elif self.cmp(key, current.key):
                current = current.left
            else:
                current = current.right
        return None

    def __getitem__(self, key: K) -> V:
        node = self.search_node(key)
        if node is not None:
            return node.value
        elif self.v_default is not None:
            value = self.v_default()
            self.insert(key, value)
            return value
        else:
            raise KeyError(key)

    def lower_bound(self, key: K) -> Optional[K]:
        current = self.root
        result = None
        while current is not None:
            if not self.cmp(current.key, key):
                result = current
                current = current.left
            else:
                current = current.right
        return result.key if result else None

    def upper_bound(self, key: K) -> Optional[K]:
        current = self.root
        result = None
        while current is not None:
            if self.cmp(key, current.key):
                result = current
                current = current.left
            else:
                current = current.right
        return result.key if result else None

    def __repr__(self) -> str:
        def _in_order_traversal(node: Optional[Node]) -> List[str]:
            if node is None:
                return []
            return (
                _in_order_traversal(node.left)
                + [f"{node.key}: {node.value}"]
                + _in_order_traversal(node.right)
            )

        items = _in_order_traversal(self.root)
        return "TreeMap({" + ", ".join(items) + "})"
